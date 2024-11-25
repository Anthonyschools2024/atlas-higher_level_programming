In this project we will eb learning about web scraping and how to implement it into our code. 
Web scraping is the process of rechreiving data from other web pages through the language of javascript.

Code Example: 

const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://www.example-ecommerce-site.com/product-page'; 

axios.get(url)
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);

    const productName = $('h1.product-title').text();
    const productPrice = $('.price').text();
    const productRating = $('.rating').text();

    console.log('Product Name:', productName);
    console.log('Price:', productPrice);
    console.log('Rating:', productRating);
  })
  .catch(error => {
    console.error('Error:', error);
  });