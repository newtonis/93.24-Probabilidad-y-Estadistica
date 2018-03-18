function [ ] = cut16( input_img,output_img,N,func )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    %CLC
    A=imread(input_img);
    B = A;

    for k=1:512/N
        f=1+(k-1)*N:k*N;
        for r=1:512/N
            c=1+(r-1)*N:r*N;
            m=func( reshape(B(f,c),[],1) );
            B(f,c) = ones(N,N)*double(m);
        end
    end

    imwrite(B,output_img);

end

