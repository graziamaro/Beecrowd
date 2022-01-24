SELECT p.name, pv.name
FROM products AS p
INNER JOIN providers AS pv on p.id_providers=pv.id
WHERE p.id_categories=6;
