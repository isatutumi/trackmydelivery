CREATE DATABASE trackmydelivery;

USE trackmydelivery;

CREATE TABLE entregas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id VARCHAR(50) NOT NULL,
    cliente VARCHAR(100) NOT NULL,
    status VARCHAR(30) NOT NULL,
    data_entrega DATE NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    atualizado_em DATETIME NOT NULL
);

ALTER TABLE entregas ADD COLUMN transportadora VARCHAR(50);

select * from entregas;