function [out ] = func_data( a,b , A)
    m = min(min(A));
    M = max(max(A));
    a = max(a,m);
    b = min(b,M);
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    out = double(a) + double(b-a)/double(M-m) * (A - m);
   
end

