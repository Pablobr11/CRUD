import mysql.connector

def conectar_banco():
    """Conecta ao banco de dados e retorna o objeto de conexão."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='bdyoutube'
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def criar_produto(nome_produto, valor):
    """Insere um novo produto no banco de dados."""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
            cursor.execute(comando, (nome_produto, valor))
            conexao.commit()
            print(f"Produto '{nome_produto}' criado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao criar produto: {err}")
        finally:
            cursor.close()
            conexao.close()

def ler_produtos():
    """Lê e exibe todos os produtos do banco de dados."""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            comando = "SELECT * FROM vendas"
            cursor.execute(comando)
            resultados = cursor.fetchall()
            if resultados:
                print("\n--- Produtos Cadastrados ---")
                for produto in resultados:
                    print(f"ID: {produto[0]}, Produto: {produto[1]}, Valor: R${produto[2]:.2f}")
                print("----------------------------")
            else:
                print("Nenhum produto cadastrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao ler produtos: {err}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(nome_produto_antigo, novo_valor):
    """Atualiza o valor de um produto existente."""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            comando = "UPDATE vendas SET valor = %s WHERE nome_produto = %s"
            cursor.execute(comando, (novo_valor, nome_produto_antigo))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"Produto '{nome_produto_antigo}' atualizado com sucesso para o valor R${novo_valor:.2f}!")
            else:
                print(f"Produto '{nome_produto_antigo}' não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar produto: {err}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(nome_produto):
    """Deleta um produto do banco de dados."""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            comando = "DELETE FROM vendas WHERE nome_produto = %s"
            cursor.execute(comando, (nome_produto,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"Produto '{nome_produto}' deletado com sucesso!")
            else:
                print(f"Produto '{nome_produto}' não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar produto: {err}")
        finally:
            cursor.close()
            conexao.close()

# --- Exemplo de como usar as funções ---
if __name__ == "__main__":
    # Exemplo de uso:
    # criar_produto("Whey Protein", 60)
    # criar_produto("Todynho", 5)
    # atualizar_produto("Todynho", 7)
    # deletar_produto("Whey Protein")
    # ler_produtos()

    # Menu interativo (opcional, para testar as funções)
    while True:
        print("\n--- Menu CRUD ---")
        print("1. Criar Produto")
        print("2. Ler Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            try:
                valor = float(input("Digite o valor do produto: "))
                criar_produto(nome, valor)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif opcao == '2':
            ler_produtos()
        elif opcao == '3':
            nome_antigo = input("Digite o nome do produto a ser atualizado: ")
            try:
                novo_valor = float(input(f"Digite o novo valor para '{nome_antigo}': "))
                atualizar_produto(nome_antigo, novo_valor)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif opcao == '4':
            nome = input("Digite o nome do produto a ser deletado: ")
            deletar_produto(nome)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")