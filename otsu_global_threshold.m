clear all,close all,clc
I = imread("rice.png");
[m,n] = size(I);
for i = 1:64:m
    for j = 1:64:n
        blk = I(i:i+63,j:j+63);
        th = 255.*graythresh(blk);
        g(i:i+63,j:j+63) = (blk>th);
    end
end
imshow(g);