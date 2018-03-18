clear;

%A=imread('lena512.bmp');




%A=imread('lena512.bmp');
 %   B = A;
%N=16;
  % for k=1:512/N
 %       f=1+(k-1)*N:k*N;
   %    for r=1:512/N
    %       c=1+(r-1)*N:r*N;
     %      mat = B(f,c,1);
      %     vec = mat(:);
           
       %    m=median( vec );
        %   B(f,c) = ones(N,N)*double(m);
       %end
   % end

  % mwrite(B,'mean_output.bmp');
do_four(4);
do_four(16);
do_four(32);
do_four(64);
