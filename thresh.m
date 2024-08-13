clear all
close all
clc
f = imread('C:\Users\BME\Desktop\IP_2024 - Copy\DIP3E_Original_Images_CH04\Fig0419(a)(text_gaps_of_1_and_2_pixels).tif');
f1 = double(f);
F = fftshift(fft2(f1));
[M,N] = size(f);
d0 = input("Enter the Cut-Off Frequency : ");
cM = M /2;
cN = N/2;
H = zeros(M,N);
for i=1:M
    for j=1:N
        d = sqrt((i-cM)^2 + (j-cN)^2);
        if d<d0
            H(i,j) = 1;
        else 
            H(i,j) = 0;
        end
    end
end
G = F.*H;
g = abs(ifft2(G));

I = imread('C:\Users\BME\Desktop\IP_2024 - Copy\DIP3E_Original_Images_CH04\Fig0419(a)(text_gaps_of_1_and_2_pixels).tif');
t = graythresh(g);
T = t * 255;
h=I>=T;
figure,imshow(h)