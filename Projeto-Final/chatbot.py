#Projeto 3 - Construindo ChatBot Personalizado com GPT-4 e Linguagem Python
#import
import openai
#chave
openai.api_key = "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"

#Função para gerar texto a partir do modelo de Linguagem
def gera_texto(texto):
    #Obtém a resposta do modelo de linguagem
    response = openai.Completion.create(
        #Modelo usado
        engine = "text-davinci-003",

        #texto inicial da conversa com o chatbor.
        prompt = texto,

        #comprimento da resposta gerada pelo modelo
        max_tokens = 150,

        #quantas conclusões gerar para cada prompt
        n = 5,

        #O texto retornado não conterá a sequencia de parada
        stop = None,

        #uma medida da aleatoriedade de um texto gerado pelo modelo. Seu valor está entre 0 e 1.
        #valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a 0 significam que a saída é muito identificável.
        temperature = 0.8,   
    )

    return response.choices[0].text.strip()

#função principal do programa em Python
def main():
    print("\nBem vindo ao GPT-4 ChatBot")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    #Loop
    while True:
        #coleta a pergunta digitada pelo usuário
        user_message = input("\nVocê: ")

        #Se a mensagem for "sair" finaliza o programa
        if user_message.lower() == "sair":
            break
        
        #Coloca a mensagem digitada pelo usuário na variável Python chamada gpt4_prompt
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

        #Obtém a resposta do modelo executando a função gera_texto()
        chatbot_response = gera_texto(gpt4_prompt)

        #Imprime a resposta do chatbot
        print(f"\nChatobot: {chatbot_response}")

#Execução do programa (bloco main) em python
if __name__ == "__main__":
    main()