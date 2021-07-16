# Caminho do executavel , caminho do arquivo, "col delimitador", "QUERY"
from App import App
import sys 
import argparse

parser = argparse.ArgumentParser("sqlinfile")

parser.add_argument("file_directory", help="String contendo o caminho absoluto do arquivo", type=str)
parser.add_argument("column_delimiter", help="String contendo o delimitador das colunas do arquivo", type=str)
parser.add_argument("query", help="String contendo a query SQL que será executada no arquivo", type=str)
parser.add_argument("skip_rows", help="Quantidade de linhas iniciais que serão ignoradas", type=int)
parser.add_argument("skip_last_rows", help="Quantidade de linhas finais que serão ignoradas", type=int)
parser.add_argument("limit_rows", help="Limita a quantidade de linhas a serem limitadas. Se = 0, retornará todas as linhas", type=int)
args = parser.parse_args()

App.init_app(args)
