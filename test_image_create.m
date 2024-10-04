clear all,close all,clc
I = zeros(256);
for i = 1:256
    for j = 1:256
        d = sqrt((128-i)^2 + (128-j)^2);
        if(d<=50)
            I(i,j) = 1;
        end
    end
end
imshow(I);
J = zeros(256);
J(78:178,78:178) = 1;
figure,imshow(J);