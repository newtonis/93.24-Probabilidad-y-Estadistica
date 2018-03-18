% Se toma la imagen %
A = imread('lena512.bmp');
S = A(:);
histogram(S);

%Continuo con los parametros de estadistica%
Media = mean(S)
Mediana = median(S)
Maximo = max(S)
Minimo = min(S)
Sprima = sort(S); %Lo ordeno Aguante Paco
PrimerQ = prctile(S,25)
%PrimerQQ = median(Sprima(find(Sprima < median(Sprima)))) (forma
%artesanal)%
TercerQ = prctile(S,75)
% Dispers = std(S) Por alguna razon, no anda el desvio estandar %
