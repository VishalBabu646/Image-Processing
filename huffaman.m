clear all,close all,clc
I = imread("cameraman.tif");
symbols = 0:255;
[m,n] = size(I);
p = zeros(1,256);
for i = 1:m
    for j = 1:n
        x = I(i,j);
        p(x+1) = p(x+1) + 1;
    end 
end
np = m * n;
probability = p /np;
i = reshape(I,1,[]);
dict = huffmandict(symbols,probability);
enco = huffmanenco(i,dict);
deco = huffmandeco(enco,dict);
y = reshape(deco,m,n);
equal = isequal(I,y)
subplot(121);imshow(I);
subplot(122);imshow(y,[]);
impixelinfo