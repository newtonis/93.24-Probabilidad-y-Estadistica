function [ ] = do_four( N )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

    
    cut16('lena512.bmp',strjoin({'data/min_output_',num2str(N),'.bmp'}),N,@min);
    cut16('lena512.bmp',strjoin({'data/mean_output_',num2str(N),'.bmp'}),N,@mean);
    cut16('lena512.bmp',strjoin({'data/median_output',num2str(N),'.bmp'}),N,@median);
    cut16('lena512.bmp',strjoin({'data/median_max',num2str(N),'.bmp'}),N,@max);
    
end

