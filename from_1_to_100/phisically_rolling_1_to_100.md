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

### d7

mantenha um d8 como counter RC e um d10 como dado normal. o dado counter começa no valor 1 e cada vez que rodar o dado normal após ter calculado o valor aumente o counter em 1. se o dado normal for maior que 7 use o valor do dado counter como valor oficial a ser usado:

   1 2 3 4 5 6 7
 1 1 1 1 1 1 1 1
 2 2 2 2 2 2 2 2
 3 3 3 3 3 3 3 3
 4 4 4 4 4 4 4 4
 5 5 5 5 5 5 5 5
 6 6 6 6 6 6 6 6
 7 7 7 7 7 7 7 7
 8 1 1 2 2 1 2 3
 9 4 5 5 4 4 3 3
10 7 6 5 6 7 7 6

ressalvas: esses tipos de dados são justos quando rodados n vezes e quando mais vezes rodados, mais justos ficam. porém eles sempre são injustos em rodadas individuais. caso a quantidade de jogadores seja a mesma que o valor máximo do dado (7 jogadores para um d7) cada jogador deve manter o seu próprio counter

obs: próximas vezes que essa tática for usada só direi qual dado é usado como RC (normalmente dois d10 formando um d100) e simplificarei a tabela para mostrar apenas o que fazer em valores anormais igual a tabela abaixo
caso tenha combinação de um ou mais dados, a tabela vem completa.

   1 2 3 4 5 6 7
 8 1 1 2 2 1 2 3
 9 4 5 5 4 4 3 3
10 7 6 5 6 7 7 6

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

### d11

mantenha um d12 como counter RC. o dado a ser usado será o d12

   1 2 3 4 5 6 7 8 9 10 11
12 1 2 3 4 5 6 7 8 9 10 11


### d12

rode um d12

r_1 : 1 2 3 4 5 6 7 8 9 10 11 12
r_1

### d13

use um d20 como counter e rode dois d4

   1  2  3  4
1  A  B  C  1
2  2  3  4  5
3  6  7  8  9
4 10 11 12 13

se o seu resultado foi A B ou C, siga a tabela abaixo de acordo com o RC e o valor rodado

   A B  C
 1 1 7 13
 2 1 7 13
 3 1 7 13
 4 2 8 11
 5 2 8 11
 6 2 9 10
 7 3 6 12
 8 3 8 10
 9 3 9  9
10 4 6 11
11 4 5 12
12 4 5 12
13 5 6 10

### d14

mantenha um d8 como counter em 7. rode um d8 e um d4

     1  2  3  4  5  6  7
1 1  1  1  1  1  1  1  1
1 2  2  2  2  2  2  2  2
1 3  3  3  3  3  3  3  3
1 4  4  4  4  4  4  4  4
1 5  5  5  5  5  5  5  5
1 6  6  6  6  6  6  6  6
1 7  7  7  7  7  7  7  7
1 8  1  2  3  4  5  6  7
2 1  8  8  8  8  8  8  8
2 2  9  9  9  9  9  9  9
2 3 10 10 10 10 10 10 10
2 4 11 11 11 11 11 11 11
2 5 12 12 12 12 12 12 12
2 6 13 13 13 13 13 13 13
2 7 14 14 14 14 14 14 14
2 8  8  9 10 11 12 13 14
3 1  1  1  1  1  1  1  1
3 2  2  2  2  2  2  2  2
3 3  3  3  3  3  3  3  3
3 4  4  4  4  4  4  4  4
3 5  5  5  5  5  5  5  5
3 6  6  6  6  6  6  6  6
3 7  7  7  7  7  7  7  7
3 8  1  2  3  4  5  6  7
4 1  8  8  8  8  8  8  8
4 2  9  9  9  9  9  9  9
4 3 10 10 10 10 10 10 10
4 4 11 11 11 11 11 11 11
4 5 12 12 12 12 12 12 12
4 6 13 13 13 13 13 13 13
4 7 14 14 14 14 14 14 14
4 8  8  9 10 11 12 13 14

### d15

rode um d6 e um d10 e siga a tabela:

r_3:
   1  2  3  4  5  6  7  8  9 10
1  1  2  3  4  5  1  2  3  4  5
2  6  7  8  9 10  6  7  8  9 10
3 11 12 13 14 15 11 12 13 14 15
4  1  2  3  4  5  1  2  3  4  5
5  6  7  8  9 10  6  7  8  9 10
6 11 12 13 14 15 11 12 13 14 15
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

rode 3 d6 e siga a tabela:


     1  2  3  4  5  6
1 1  1  2  3  1  2  3
1 2  4  5  6  4  5  6
1 3  7  8  9  7  8  9
1 4  1  2  3  1  2  3
1 5  4  5  6  4  5  6
1 6  7  8  9  7  8  9
2 1 10 11 12 10 11 12
2 2 13 14 15 13 14 15
2 3 16 17 18 16 17 18
2 4 10 11 12 10 11 12
2 5 13 14 15 13 14 15
2 6 16 17 18 16 17 18
3 1 19 20 21 19 20 21
3 2 22 23 24 22 23 24
3 3 25 26 27 25 26 27
3 4 19 20 21 19 20 21
3 5 22 23 24 22 23 24
3 6 25 26 27 25 26 27
4 1  1  2  3  1  2  3
4 2  4  5  6  4  5  6
4 3  7  8  9  7  8  9
4 4  1  2  3  1  2  3
4 5  4  5  6  4  5  6
4 6  7  8  9  7  8  9
5 1 10 11 12 10 11 12
5 2 13 14 15 13 14 15
5 3 16 17 18 16 17 18
5 4 10 11 12 10 11 12
5 5 13 14 15 13 14 15
5 6 16 17 18 16 17 18
6 1 19 20 21 19 20 21
6 2 22 23 24 22 23 24
6 3 25 26 27 25 26 27
6 4 19 20 21 19 20 21
6 5 22 23 24 22 23 24
6 6 25 26 27 25 26 27
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
r_3 = (r_1 - 1) * 10 + r_2

### d45

rode dois d6 e um d10

     1  2  3  4  5  6  7  8  9 10
1 1  1  2  3  4  5  1  2  3  4  5
1 2  6  7  8  9 10  6  7  8  9 10
1 3 11 12 13 14 15 11 12 13 14 15
1 4  1  2  3  4  5  1  2  3  4  5
1 5  6  7  8  9 10  6  7  8  9 10
1 6 11 12 13 14 15 11 12 13 14 15
2 1 16 17 18 19 20 16 17 18 19 20
2 2 21 22 23 24 25 21 22 23 24 25
2 3 26 27 28 29 30 26 27 28 29 30
2 4 16 17 18 19 20 16 17 18 19 20
2 5 21 22 23 24 25 21 22 23 24 25
2 6 26 27 28 29 30 26 27 28 29 30
3 1 31 32 33 34 35 31 32 33 34 35
3 2 36 37 38 39 40 36 37 38 39 40
3 3 41 42 43 44 45 41 42 43 44 45
3 4 31 32 33 34 35 31 32 33 34 35
3 5 36 37 38 39 40 36 37 38 39 40
3 6 41 42 43 44 45 41 42 43 44 45
4 1  1  2  3  4  5  1  2  3  4  5
4 2  6  7  8  9 10  6  7  8  9 10
4 3 11 12 13 14 15 11 12 13 14 15
4 4  1  2  3  4  5  1  2  3  4  5
4 5  6  7  8  9 10  6  7  8  9 10
4 6 11 12 13 14 15 11 12 13 14 15
5 1 16 17 18 19 20 16 17 18 19 20
5 2 21 22 23 24 25 21 22 23 24 25
5 3 26 27 28 29 30 26 27 28 29 30
5 4 16 17 18 19 20 16 17 18 19 20
5 5 21 22 23 24 25 21 22 23 24 25
5 6 26 27 28 29 30 26 27 28 29 30
6 1 31 32 33 34 35 31 32 33 34 35
6 2 36 37 38 39 40 36 37 38 39 40
6 3 41 42 43 44 45 41 42 43 44 45
6 4 31 32 33 34 35 31 32 33 34 35
6 5 36 37 38 39 40 36 37 38 39 40
6 6 41 42 43 44 45 41 42 43 44 45
r_4 = (r_1 % 3) * 15 + (r_2 % 3) * 5 + r_3 % 5


### d48

rode um d6 e um d8

   1  2  3  4  5  6  7  8
1  1  2  3  4  5  6  7  8
2  9 10 11 12 13 14 15 16
3 17 18 19 20 21 22 23 24
4 25 26 27 28 29 30 31 32
5 33 34 35 36 37 38 39 40
6 41 42 43 44 45 46 47 48
r_3 = (r_1 - 1) * 8 + r_2

### d50 : 

rode 2 d10

    1  2  3  4  5  6  7  8  9 10
 1  1  2  3  4  5  6  7  8  9 10
 2 11 12 13 14 15 16 17 18 19 20
 3 21 22 23 24 25 26 27 28 29 30
 4 31 32 33 34 35 36 37 38 39 40
 5 41 42 43 44 45 46 47 48 49 50
 6  1  2  3  4  5  6  7  8  9 10
 7 11 12 13 14 15 16 17 18 19 20
 8 21 22 23 24 25 26 27 28 29 30
 9 31 32 33 34 35 36 37 38 39 40
10 41 42 43 44 45 46 47 48 49 50
r_3 = (r_1 % 5) * 10 + r_2

### d54 : roll 1d6 and 1d9 (3d6)
### d60 : roll 1d10 and 1d6
### d64 : roll 2d8
### d72 : roll 1d6 and 1d12
### d75 : roll 1d5 and 1d15 (2d10 + 1d6) 
### d80 : roll 1d10 and 1d8
### d81 : roll 2d9 (4d6)
### d90 : roll 1d10 and 1d9 (2d6 + 1d10)
### d96 : roll 1d8 and 1d12
### d100 : roll 2d10