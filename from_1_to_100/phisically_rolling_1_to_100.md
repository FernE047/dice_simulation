# Rodando dados de 1 a 100 faces

Se a ideia for rodar dados de 1 a 100 faces só utilizando d4, d6, d8, d10, d12 e d20 da maneira mais simples possivel para alguém fazzer fisicamente temos que simplificar alguns casos

esse já são os casos mais simples:

d1 : roll any dice, r mod 1 + 1
d2 : roll d4, r mod 2 + 1
d3 : roll d6, r mod 3 + 1
d4 : roll d4
d5 : roll d10, r mod 5 + 1
d6 : roll d6
d8 : roll d8
d9 : roll 2d3, r_1*3 + r_2
d10 : roll d10
d12 : roll d12
d15 : roll 1d3 and 1d5, r_1*5 + r_2
d16 : roll 2d4
d18 : roll 1d3 and 1d6
d20 : roll d20
d24 : roll 1d2 and 1d6
d25 : roll 2d5
d27 : roll 1d3 and 1d9
d30 : roll 1d5 and 1d6
d32 : roll 1d8 and 1d4
d36 : roll 2d6
d40 : roll 1d5 and 1d8
d45 : roll 1d9 and 1d5
d48 : roll 1d4 and 1d12
d50 : roll 1d5 and 1d10
d54 : roll 1d3 and 1d18
d60 : roll 1d5 and 1d12
d64 : roll 2d8
d72 : roll 1d6 and 1d12
d75 : roll 1d5 and 1d15
d80 : roll 1d5 and 1d16
d81 : roll 1d3 and 1d27
d90 : roll 1d5 and 1d18
d96 : roll 1d8 and 1d12
d100 : roll 2d10

nessa exploração do problema só queremos deixar o mais simples possivel para o player, contanto que ainda seja justo

## Manual

### d1

rode um d4 e divida o resultado r_1 pelo resultado r_1:

r_1 : 1 2 3 4
r_2 : 1 1 1 1
r_2 = r_1 / r_1

### d2

rode um d4 se o r_1 e faça mod 2 + 1

r_1 : 1 2 3 4
r_2 : 1 2 1 2
r_2 = r_1 % 2 + 1

### d3

rode um d6 se o r_1 e faça mod 3 + 1

r_1 : 1 2 3 4 5 6
r_2 : 1 2 3 1 2 3
r_2 = r_1 % 3 + 1

### d4

rode um d4.

r_1 : 1 2 3 4
r_1

### d5

rode o d10 e faça mod 5 + 1

r_1 : 1 2 3 4 5 6 7 8 9 10
r_2 : 1 2 3 4 5 1 2 3 4  5
r_2 = r_1 % 5 + 1

### d6

rode o d6.

r_1 : 1 2 3 4 5 6
r_1

### d8

rode um d8

r_1 : 1 2 3 4 5 6 7 8
r_1

### d9

rode dois d6 e siga a tabela:

r_3:
  1 2 3 4 5 6
1 1 2 3 1 2 3
2 4 5 6 4 5 6
3 7 8 9 7 8 9
4 1 2 3 1 2 3
5 4 5 6 4 5 6
6 7 8 9 7 8 9
r_3 = (r_1 % 3) * 3 + r_2 % 3 + 1

### d10

rode um d10

r_1 : 1 2 3 4 5 6 7 8 9 10
r_1

### d12

rode um d12

r_1 : 1 2 3 4 5 6 7 8 9 10 11 12
r_1

### d15

rode um d6 e um d5 e siga a tabela:

r_3:
   1  2  3  4  5
1  1  2  3  4  5
2  6  7  8  9 10
3 11 12 13 14 15
4  1  2  3  4  5
5  6  7  8  9 10
6 11 12 13 14 15
r_3 = (r_1 % 3) * 5 + r_2 % 5 + 1

### d16

rode dois d4 e siga a tabela:

r_3:
   1  2  3  4
1  1  2  3  4
2  5  6  7  8
3  9 10 11 12
4 13 14 15 16
r_3 = (r_1 - 1) * 4 + r_2

### d18

rode dois d6 e siga a tabela:

r_3:
   1  2  3  4  5  6
1  1  2  3  4  5  6
2  7  8  9 10 11 12
3 13 14 15 16 17 18
4  1  2  3  4  5  6
5  7  8  9 10 11 12
6 13 14 15 16 17 18
r_3 = (r_1 % 3) * 3 + r_2

### d20

rode um d12

r_1 : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
r_1

### d24

rode um d4 e um d6 e siga a tabela:

r_3
   1  2  3  4  5  6
1  1  2  3  4  5  6
2  7  8  9 10 11 12
3 13 14 15 16 17 18
4 19 20 21 22 23 24
r_3 = (r_1 - 1) * 6 + r_2

### d25

rode dois d10 e siga a tabela:

r_3:
    1  2  3  4  5  6  7  8  9 10
 1  1  2  3  4  5  1  2  3  4  5
 2  6  7  8  9 10  6  7  8  9 10
 3 11 12 13 14 15 11 12 13 14 15
 4 16 17 18 19 20 16 17 18 19 20
 5 21 22 23 24 25 21 22 23 24 25
 6  1  2  3  4  5  1  2  3  4  5
 7  6  7  8  9 10  6  7  8  9 10
 8 11 12 13 14 15 11 12 13 14 15
 9 16 17 18 19 20 16 17 18 19 20
10 21 22 23 24 25 21 22 23 24 25
r_3 = (r_1 % 5) * 5 + r_2 % 5 + 1

### d27

rode 3 d6 e siga a tabela de acordo com o resultado do primeiro d6:

r_1 é 1 ou 4:
  1 2 3 4 5 6
1 1 2 3 1 2 3
2 4 5 6 4 5 6
3 7 8 9 7 8 9
4 1 2 3 1 2 3
5 4 5 6 4 5 6
6 7 8 9 7 8 9

r_1 é 2 ou 5:
   1  2  3  4  5  6
1 10 11 12 10 11 12
2 13 14 15 13 14 15
3 16 17 18 16 17 18
4 10 11 12 10 11 12
5 13 14 15 13 14 15
6 16 17 18 16 17 18

r_1 é 2 ou 5:
   1  2  3  4  5  6
1 19 20 21 19 20 21
2 22 23 24 22 23 24
3 25 26 27 25 26 27
4 19 20 21 19 20 21
5 22 23 24 22 23 24
6 25 26 27 25 26 27

r_4 = (r_1 % 3) * 9 + (r_2 % 3) * 3 + r_3 % 3

### d30

rode um d6 e um d10 e siga a tabela

r_3 :
    1  2  3  4  5  6
 1  1  2  3  4  5  6
 2  7  8  9 10 11 12
 3 13 14 15 16 17 18
 4 19 20 21 22 23 24
 5 25 26 27 28 29 30
 6  1  2  3  4  5  6
 7  7  8  9 10 11 12
 8 13 14 15 16 17 18
 9 19 20 21 22 23 24
10 25 26 27 28 29 30
r_3 = (r_1 % 5) * 6 + r_2


### d32

rode um d4 e um d8 e siga a tabela

r_3
    1  2  3  4  5  6  7  8
 1  1  2  3  4  5  6  7  8
 2  9 10 11 12 13 14 15 16
 3 17 18 19 20 21 22 23 24
 4 25 26 27 28 29 30 31 32
r_3 = (r_1 - 1) * 8 + r_2

### d36

rode dois d6 e siga a tabela:

r_3:
   1  2  3  4  5  6
1  1  2  3  4  5  6
2  7  8  9 10 11 12
3 13 14 15 16 17 18
4 19 20 21 22 23 24
5 25 26 27 28 29 30
6 31 32 33 34 35 36
r_3 = (r_1 - 1) * 6 + r_2

### d40

rode um d4 e um d10 e siga a tabela:
   1  2  3  4  5  6  7  8  9 10
1  1  2  3  4  5  6  7  8  9 10
2 11 12 13 14 15 16 17 18 19 20
3 21 22 23 24 25 26 27 28 29 30
4 31 32 33 34 35 36 37 38 39 40

### d45 : 3 * 15
### d48 : roll 1d4 and 1d12
### d50 : roll 1d5 and 1d10
### d54 : roll 1d3 and 1d18
### d60 : roll 1d5 and 1d12
### d64 : roll 2d8
### d72 : roll 1d6 and 1d12
### d75 : roll 1d5 and 1d15
### d80 : roll 1d5 and 1d16
### d81 : roll 1d3 and 1d27
### d90 : roll 1d5 and 1d18
### d96 : roll 1d8 and 1d12
### d100 : roll 2d10

## d7

considere o round counter = RC

rode um d4 se o r_1 é maior que 2 subtraia por 2 para obter o resultado r_2

r_1 : 1 2 3 4
r_2 : 1 2 1 2
r_2 = r_1 - 2 * k

### r_2=1

se o r_2 for 1; rode um d6 para obter r_3, se r_3 é maior que 3 subtraia por 3 para obter r_4

r_3 : 1 2 3 4 5 6
r_4 : 1 2 3 1 2 3
r_4 = r_3 - 3 * k

adicione o RC e se o resultado for maior que 7 subtraia por 7

r_5 :

  1 2 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
5 6 7 1
6 7 1 2
7 1 2 3

r_5 = r_4 + RC - 7 * k

### r_2=2

se o r_2 for 2; rode um d4 e adicione 3 para obter r_4

r_3 : 1 2 3 4
r_4 : 4 5 6 7
r_4 = r_3 + 3

adicione o RC e se o resultado for maior que 7 subtraia por 7

r_5 :

  4 5 6 7
1 5 6 7 1
2 6 7 1 2
3 7 1 2 3
4 1 2 3 4
5 2 3 4 5
6 3 4 5 6
7 4 5 6 7

r_5 = r_4 + RC - 7 * k
ou
r_5 = r_3 + 3 + RC - 7 * k


## d11

rode um d4 se o r_1 é maior que 2 subtraia por 2 para obter o resultado r_2

r_1 : 1 2 3 4
r_2 : 1 2 1 2
r_2 = r_1 - 2 * k

### r_2=1

se o r_2 for 1; rode um d10 para obter r_3, se r_3 é maior que 5 subtraia por 5 para obter r_4

r_3 : 1 2 3 4 5 6 7 8 9 10
r_4 : 1 2 3 4 5 1 2 3 4  5
r_4 = r_3 - 5 * k

adicione o RC e se o resultado for maior que 11 subtraia por 11

r_5 :

    1  2  3  4  5
1   2  3  4  5  6
2   3  4  5  6  7
3   4  5  6  7  8
4   5  6  7  8  9
5   6  7  8  9 10
6   7  8  9 10 11
7   8  9 10 11  1
8   9 10 11  1  2
9  10 11  1  2  3
10 11  1  2  3  4
11  1  2  3  4  5
r_5 = r_4 + RC - 11 * k

### r_2=2

se o r_2 for 2; rode um d6 e adicione 5 para obter r_4

r_3 : 1 2 3 4  5  6
r_4 : 6 7 8 9 10 11
r_4 = r_3 + 5

adicione o RC e se o resultado for maior que 11 subtraia por 11

r_5 :

    6  7  8  9 10 11
1   7  8  9 10 11  1
2   8  9 10 11  1  2
3   9 10 11  1  2  3
4  10 11  1  2  3  4
5  11  1  2  3  4  5
6   1  2  3  4  5  6
7   2  3  4  5  6  7
8   3  4  5  6  7  8
9   4  5  6  7  8  9
10  5  6  7  8  9 10
11  6  7  8  9 10 11

r_5 = r_4 + RC - 11 * k
ou
r_5 = r_3 + 5 + RC - 11 * k