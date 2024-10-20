from openai import OpenAI
import typer
from rich import print
from rich.table import Table





def main ():
    
    client = OpenAI()
    
    print("[bold green]ChatGPT API en Python[/bold green]")
    
    table = Table("Comando","Descripcion")
    
    table.add_row("exit","Salir de la aplicacion")
    table.add_row("new","Crear una nueva conversacion")
    
    print(table)

    #CONTEXTO DE GPT
    context = {"role":"system","content":"Eres un asistente especialista en inteligencia artificial"}
    
    messages = [context]

    while True:

        content = __prompt()
        
        if content == "new":
            print("Nueva conversion!!")
            messages = [context]
            content = __prompt()
        

        messages.append({"role": "user","content": content})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        
        response_content = response.choices[0].message.content
        
        messages.append({"role":"assistant","content":response_content})

        print(f"[bold green] > [/bold green] [green]{response_content}[/green]")
         
        
def __prompt() -> str:
    prompt = typer.prompt("\nSobre que queres hablar? ")
    
    if prompt == "exit":
        exit = typer.confirm("Estas seguro?")
        if exit:
            print("Hasta luego!!")
            raise typer.Abort()
        return __prompt()
    
    return prompt

if __name__ == "__main__":
    typer.run(main)
