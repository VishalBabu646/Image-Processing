clear all, close all, clc
I = imread("cameraman.tif");
[m,n] = size(I);
for i=1:m
    for j=1:n
        r = I(i,j);
        if(r < 120)
            s(i,j)= 0;
        elseif(r > 120 && r < 160)
                s(i,j) = 120;
        else
            s(i,j) = 256;
        end
    end
end
figure,imshow(s)
       
