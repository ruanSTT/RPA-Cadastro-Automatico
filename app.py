import pyautogui 
from time import sleep

# 1 - Clicar e digitar meu usuário;
pyautogui.click(817,452,duration=2)
pyautogui.write('Ruan')
# 2 - Clicar e digitar minha senha;
pyautogui.click(819,477,duration=2)
pyautogui.write('1234')
# 3 - Clicar em entrar;
pyautogui.click(705,511,duration=2)
# 4 - Extrair cada produto:
with open ('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 	1 - Clicar e digitar o produto;   
        pyautogui.click(549,437,duration=2)
        pyautogui.write(produto)
        # 	2 - Clicar e digitar a quantidade;
        pyautogui.click(534,465,duration=2)
        pyautogui.write(quantidade)
        # 	3 - Clicar e digitar preço;
        pyautogui.click(532,491,duration=2)
        pyautogui.write(preco)
        # 	4 - Clicar em registrar.
        pyautogui.click(445,649, duration=1)
        sleep(1)