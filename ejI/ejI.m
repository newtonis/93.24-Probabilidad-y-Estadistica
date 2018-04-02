
A=imread('lena512.bmp');

B = reshape(A,[],1);

mu = median(B);
s = std(double(B));
 
arr = [0.5,1,2];
for ri=1:length(arr)
 r = arr(ri);
 
 info = func_data(mu - r * s , mu + r * s,A);
 
 imwrite( info, strjoin({'output_',int2str(ri),'.bmp'}));
 
end
 
 