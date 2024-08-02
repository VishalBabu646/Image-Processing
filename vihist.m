function h = vihist(I)
[r,c] = size(I);
h = zeros(1,256);
for i = 1:r
    for j =1:c
        temp = I (i,j);
        h(temp) = h(temp) + 1;
    end 
end
end




