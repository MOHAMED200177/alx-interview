function rotate_2d_matrix(matrix) {
    const c = matrix.length;

    for (let i = 0; i < c; i++) {
        for (let j = i; j < c; j++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    for (let i = 0; i < c; i++) {
        matrix[i].reverse();
    }
}

const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
rotate_2d_matrix(matrix);
console.log(matrix);