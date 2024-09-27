clear all,close all,clc
I = imread('C:\Users\Administrator\Desktop\IP Lab images 2023\test14.tif');
a = [0,1,0;1,-4,1;-0,1,0];
f = imfilter(I,a);
imshow(f);
[m,n] = size(f);
R = zeros(m,n);
for i = 1:m
    for j=1:n
        if f(i,j) >= 200
            R(i,j) = 1;
        else
            R(i,j) = 0;
        end
    end
end
figure,imshow(R);
