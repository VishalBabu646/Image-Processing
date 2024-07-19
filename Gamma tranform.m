clear all,close all,clc
I = imread("cameraman.tif");
[m,n] = size(I);
c = 1;
g = 0.2;
r = double(I);
for i = 1:m
    for j = 1:n
        s(i,j) = c * ( r(i,j) ^ g);
        T = 255/(c * 255 ^g);
    end
end
figure,imshow(uint8(s * T))
