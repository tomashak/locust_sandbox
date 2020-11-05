use prestashop;

show tables;

select * from ps_cart order by id_cart desc limit 1;
select * from ps_cart_product where id_cart=6;
select ps_cart_product.*,ps_product.price,ps_product_lang.name,ps_product_lang.description_short from ps_cart_product 
join ps_product ON ps_cart_product.id_product=ps_product.id_product
join ps_product_lang ON ps_cart_product.id_product=ps_product_lang.id_product
where ps_cart_product.id_cart=6;

select * from ps_product where id_product=1;
select * from ps_product_shop where id_product=1;
select * from ps_product_attribute where id_product=1;
select * from ps_product_lang where id_product=1;
select * from ps_product_attribute_image;
select * from ps_product_attribute_shop;
select * from ps_product_attribute_combination;
