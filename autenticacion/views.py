from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from autenticacion.serializer import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from autenticacion.models import Usuario
from rest_framework import status


# Create your views here.
@api_view(["POST"])
def registro(request):
    serializer = UsuarioSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = Usuario.formatear_username(
        serializer.validated_data["primer_apellido"],
        serializer.validated_data["segundo_apellido"],
        serializer.validated_data["primer_nombre"],
        serializer.validated_data["segundo_nombre"]
    )

    if Usuario.existe(username):
        return Response({"error": "La cuenta ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    email = serializer.validated_data["email"]

    if Usuario.email_existe(email):
        return Response({"error": "El correo ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    usuario = Usuario(**serializer.validated_data)

    usuario.username = username
    usuario.set_password(serializer.validated_data["password"])
    usuario.email = serializer.validated_data["email"]
    usuario.save()  # Guardar el usuario después de encriptar la contraseña


    token = Token.objects.create(user=usuario)

    return Response({"token": token.key, "user": serializer.data},status=status.HTTP_201_CREATED)


# LOGIN
@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    print(f"Intentando iniciar sesion con {email}")

    if not Usuario.email_existe(email):
        print("Correo no encontrado en la BD")
        return Response({"error": "El correo no existe"}, status=status.HTTP_401_UNAUTHORIZED)


    usuario = Usuario.objects.get(email=email)
    print(f"Usuario encontrado {usuario.username}")

    print(f"Contraseña recibida: {password}")

    if not usuario.check_password(password):
        return Response({"error": "La contraseña es incorrecta o no se ha ingresado"}, status=status.HTTP_401_UNAUTHORIZED)

    
    
    token, created = Token.objects.get_or_create(user=usuario)
    serializer = UsuarioSerializer(instance=usuario)

    return Response({"token": token.key,
                      "user": serializer.data,
                      "role":"admin" if usuario.is_superuser else "user"}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    token = request.auth

    if not token:
        return Response({"error": "No se encontró el token de autenticación"}, status=status.HTTP_400_BAD_REQUEST)

    token.delete()

    return Response({"message": "Sesión cerrada exitosamente"}, status=status.HTTP_200_OK)