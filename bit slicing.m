clear all, close all,clc
I = imread("cameraman.tif");
n = 8;
B = bitget(I,n);
figure,imshow(logical(B))
for i=1:8
    B = bitget(I,i);
    subplot(4,2,i);
    imshow(logical(B))
    title(['Bit Plane ' num2str(i)]);
    
end