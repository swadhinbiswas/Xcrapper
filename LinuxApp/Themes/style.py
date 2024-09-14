from rich.console import Console
from rich.progress import track, Progress
from rich.table import Table
from rich.panel import Panel
from rich.style import Style
from rich.align import Align
from time import sleep
from rich.markdown import Markdown
from rich import box
from rich.text import Text





class TextStyle:
    def __init__(self):
        self.console = Console()
        
    def print_app_title(self):
        self.console.print(Panel("Twitter CLI App by @swadhinbiswas :vampire:", style="bold blue", title="Welcome to Twitter CLI App", title_align="center"), justify="center")
    
    def track_progress(self, iterable):
        for i in track(iterable, description="Processing..."):
            sleep(0.01)
            
    def print_table(self, data, title):
        table = Table(title=title)
        for key, value in data.items():
            table.add_column(key, style="cyan", no_wrap=True, justify="left")
            table.add_row(str(value), style="magenta")
            
        self.console.print(table)
        
    def print_markdown(self, data):
        self.console.print(Markdown(data))
    
    def print_error(self, message):
        self.console.print(Panel(message, title="Error", title_align="center", style="bold red"))
    def print_success(self, message):
        self.console.print(Panel(message, title="Success", title_align="center", style="bold green"))
    def print_warning(self, message):
        self.console.print(Panel(message, title="Warning", title_align="center", style="bold yellow"))
        
    def print_info(self, message):
        self.console.print(Panel(message, title="Info", title_align="center", style="bold blue"))
    def print_help(self, message):
        self.console.print(Panel(message, title="Help", title_align="center", style="bold blue"))
    def print_question(self, message):
        self.console.print(Panel(message, title="Question", title_align="center", style="bold blue"))
    def printtext(self, message):
        text=Text(message, style="bold blue")
        self.console.print(text, justify="center")
    
    def choose_option(self):
        self.console.print(Panel("Please choose an option: ", style="bold blue", title="Choice", title_align="center"))
        
    def print_option(self, option, text):
        self.console.print(f"[{option}] {text}")
        
    def print_input(self, message):
        self.console.print(Panel(message, style="bold blue", title="Input", title_align="center"))
        
    def print_output(self, message):
        self.console.print(Panel(message, style="bold blue", title="Output", title_align="center"))
    def print_line(self):
        self.console.print(Panel("", style="bold blue", title="_______x__________________x________________x____________x____________", title_align="center"))
    
    def welcome(self):
        console=self.console
        # Additional space
       
        welcome_text = Text("Welcome to Twitter! 🐦\n", style="bold magenta")
        
        instruction_text = Text("Please choose an option:\n", style="italic yellow",justify= "center")
        text=Text.assemble(welcome_text, instruction_text)
        console.print(text,justify="center")


