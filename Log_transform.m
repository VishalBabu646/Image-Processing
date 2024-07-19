clear all,close all,clc
I = imread("cameraman.tif");
[m,n] = size(I);
c = 1;
r = double(I);
for i = 1:m
    for j = 1:n
        s(i,j) = c * log(1 + r(i,j));
        T = 255/(c * log(256));
    end
end
figure,imshow(uint8(s * T))


