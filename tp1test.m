
A = imread('lena512.bmp');

S = A(:);

#q = statistics(S);

#minimo = q(1);
#q1 = q(2);
#mediana = q(3);
#q3 = q(4);
#maximo = q(5);
#media = q(6);
#sta_deviation = q(7);
truc={"Id", "Name", "Type";1, "onestring", "bla"; 2, "somestring", "foobar";}
dataframe(truc);