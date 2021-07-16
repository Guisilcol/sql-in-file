from modules.Menu.menu import Menu 
from modules.Parsers.FileParser import FileParser

class App: 
    
    def init_app(args):
        Menu.show_logo()
        
        file_parser = FileParser(file_directory=args.file_directory
                                 ,column_delimiter=args.column_delimiter
                                 ,skip_last_rows=args.skip_last_rows
                                 ,skip_rows=args.skip_rows
                                 ,limit_rows=args.limit_rows)
        
        file_parser.read_file_to_dataframe()
        print(file_parser.execute_sql_in_dataframe(args.query))
        
