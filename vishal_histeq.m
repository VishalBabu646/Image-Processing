clear all,close all,clc
I = imread('C:\Users\BME\Desktop\IP_2024 - Copy\DIP3E_Original_Images_CH03\Fig0316(2)(2nd_from_top).tif');
[r,c] = size(I);
h = zeros(1,256);
for i = 1:r
    for j =1:c
        temp = I (i,j);
        h(temp) = h(temp) + 1;
    end 
end
imshow(I)
figure,plot(h)
