clear all, close all,clc
I = imread("cameraman.tif");
L = 2 ^ 8;
[m,n] = size(I);
for i = 1:m
    for j = 1:n
        r = I(i,j);
        s(i,j) = L - r;
    end
end
imshow(s)