from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    os.system("cls || clear")

    # Solicitando dados para o usuário.
    print("\nAdicionado Usuário.")
    nome = input("Digite seu nome:")
    email = input("Digite seu e-mail:")
    senha = input("Digite sua senha:")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usuários cadastrados
    print("\nListar usuários cadastrados")
    listar_usuarios = service.listar_todos_usuarios()
    for usuario in listar_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")


if __name__ == "__main__":
    main()
