clc;

A = imread('lena512.bmp');
%imshow(A);

len=length(A);

MeanVector = 1:len;
MaxVector = 1:len;
MinVector = 1:len;
FirstQuantile = 1:len;
ThirdQuantile = 1:len;
MedianVec = 1:len;

for i=1:len
sort(A(i,:));
MeanVector(i) = mean(A(i,:));  %extraigo la iesima fila y le aplico mean a ese vector
MaxVector(i) = max(A(i,:));
MinVector(i) = min(A(i,:));
FirstQuantile(i) = quantile(A(i,:),0.25);
ThirdQuantile(i) = quantile(A(i,:),0.75);
MedianVec(i) = median(A(i,:));
end

%descomentamos en función de lo que queremos ver
%U=MedianVec;
%U=MeanVector;
U=FirstQuantile;
%U=ThirdQuantile;




B=A;

for k = 1:len
    for l= 1:len
        B(k,l) = 255 * (A(k,l)>U(k));
    end
end

imshow(B);

