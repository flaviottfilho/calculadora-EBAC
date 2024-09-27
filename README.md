# calculadora-EBAC
 Calculator developed as an assignment for the Data Analyst course at EBAC

## INSTRUCTIONS-EN 

- You **MUST** keep both "calculadora.sh" and "calculadora.py" in the same folder for it to work properly.

1. Locate the directory where you downloaded the .zip file.

2. Extract the files to a directory of your choosing.

3. Open your favorite terminal emulator, locate the directory where you extracted the files to and execute "calculadora.sh".

4. Wait for the updates to finish, if there are any.

5. Choose one of the 4 available operations to perform. (Refer to the table below)

6. Insert the first number, then the second number.

7. Get your result!


### Supported Operations

| Option | Operation |
| ----------- | ----------- |
| 1 | addition |
| 2 | subtraction |
| 3 | Division |
| 4 | Multiplication |


## INSTRUÇÕES-BR

- Você **DEVE** manter ambos arquivos "calculadora.sh" e "calculadora.py" no mesmo arquivo para que o programa  funcione apropriadamente.

1. Localize o diretório onde salvou o arquivo.zip

2. Extraia os arquivos para o diretório de sua preferência.

3. Abra seu terminal preferido, localize o diretório para onde extraiu os arquivos e execute "calculadora.sh"

4. Aguarde a conclusão das atualizações, caso ocorra alguma, e siga as instruções da tela!

### Operações Suportadas

| Opção | Operação |
| ----------- | ----------- |
| 1 | adição |
| 2 | subtração |
| 3 | Divisão |
| 4 | Multiplicação |



# Into the Code

I started the code with a "while True" loop to make sure the user can only proceed after selecting one of the valid 4 options offered by the program. I then used a "if" conditional to raise a ValueError if the user inputs anything other than the numbers 1, 2, 3 or 4.

After picking an option, the user will be prompted to input the first number, then the second number. I also used a "while True" loop on both entries to ensure the user inputs a number.

After performing the operation with both numbers, the result is printed on the screen and the program is terminated.


# Dentro do Código

Iniciei o código com um loop "while True" para ter certeza que o usuário apenas consiga proceder depois de selecionar uma das quatro opções válidas oferecidas pelo programa. Então usei uma condicional "if" para levantar um ValueError caso o usuário insira qualquer coisa além dos números 1, 2, 3 ou 4.

Depois de escolher uma opção, o programa irá pedir que o usuário insira o primeiro número, e então o segundo número. eu também usei um loop "while True" em ambas as entradas para assegurar que o usuário insira um número.

Depois de realizar a operação com ambos os números, o resultado é mostrado na tela e o programa, encerrado.
