CREATE TABLE donations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_gardian VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    dateOfBirth DATETIME,
    bloodGroup VARCHAR(5),
    organ VARCHAR(50),
    addressline1 VARCHAR(255),
    addressline2 VARCHAR(255),
    state VARCHAR(50),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    dateOfBirth DATETIME,
    bloodGroup VARCHAR(5),
    organ VARCHAR(50),
    addressline1 VARCHAR(255),
    addressline2 VARCHAR(255),
    state VARCHAR(50),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
