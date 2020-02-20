x = zeros(Int8, 5, 10)
for j = 1:10   # inner loop: last dim
    for i = 1:5  # outer loop: 1st dim
        println(x[i, j])
    end
end
