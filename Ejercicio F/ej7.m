clc;

iscol = 1;
if iscol
    A = imread('lena512.bmp');
    imshow(A);
else
    B=imread('lena512.bmp');
    A=B';    
    imshow(A);
end

len=length(A);

MeanVector = 1:len;
MaxVector = 1:len;
MinVector = 1:len;
FirstQuantile = 1:len;
ThirdQuantile = 1:len;

for i=1:len
MeanVector(i) = mean(A(i,:));  %extraigo la iesima columna y le aplico mean a ese vector
MaxVector(i) = max(A(i,:));
MinVector(i) = min(A(i,:));
FirstQuantile(i) = quantile(A(i,:),0.25);
ThirdQuantile(i) = quantile(A(i,:),0.75);
end

%descomentamos en función de lo que queremos ver

plot(MeanVector);
%plot(MaxVector);
%plot(MinVector);
%plot(FirstQuantile);
%plot(ThirdQuantile);
%boxplot(A);
