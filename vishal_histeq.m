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
% normalised histogram = PDF
n = r*c;
hn = h/n;
skd(1) = hn(1);
for k = 2:256
    skd(k) = hn(k) + skd(k -1);
end 
sk = skd.*255;
sk = round(sk);
rk =0:255;
figure,plot(rk,sk)
%Applying the transform
for i=1:r
    for j=1:c
        t = I(i,j);
        g(i,j) = sk(t+1);
    end
end
g = uint8(g);
figure,imshow(g)
[r1,c1] = size(g);
h1 = zeros(1,256);
for i = 1:r1
    for j =1:c1
        temp = g (i,j);
        h1(temp) = h1(temp) + 1;
    end 
end

