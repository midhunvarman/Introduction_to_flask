# HTML

## Introduction to HTML
HTML stands for hypertext markup language used to make the skeleton or framework of a webpage.
The latest version is HTML 5 and there are software which need to be installed, everything is preinstalled.

```
<!DOCTYPE html>

<html lang="en">

<HTML>

<head>

<title> Page Title </title>

</head>

<body>


<h1> This is a Heading </h1>

<p> This is a Paragraph </p>


</body>

</html>
```

- `<!DOCTYPE>` The doctype declaration indicates the document type and version of HTML used on the webpage. Each HTML version has a different doctype declaration. HTML5 Doctype is used in this example.
- `<html>` The HTML tag is the root tag that describes the whole webpage. It is a paired tag, i.e., it has a closing tag also, `</html>`. Everything will be written inside these tags.
- `<head>` Head tag contains information about the document like its title, author information, description of the webpage, and so on. It has different tags to perform these functions. It is also a paired tag.
- `<title>` Title tag is used inside <head>, and it specifies the title of the document.
- `<body>` The body tag contains all the information which will be displayed on the webpage. If you want anything to be displayed on the webpage, you have to write it within these tags.
- `<h1>` Heading tag is used to define headings. `<h1>` is the largest heading, followed by `<h2>`, `<h3>`, to `<h6>`.


## HTML Tags
HTML Tags: The whole HTML functions on HTML Tags. These HTML tags are the basic building block of a website. Without these tags, there would be no website. No web technologies like CSS, PHP, Python, wordpress, etc. will exist without HTML Tags. These are the driving force of the internet. So, the question is, what is an HTML Tag? Let's find out!

### What is HTML Tag?
TML Tags are pre-defined elements in HTML, enclosed within these < > signs. 
```For example: <html>, <table>, etc. ```
All HTML tags have a particular work associated with them. Each one has a special function and a combination of various tags forms a website. For example, a < p > tag defines a paragraph in the website and a < table > tag displays a table.

All HTML Tags are predefined, i.e., you cannot make HTML tags by yourself. Look at the example below, this is an example of a paired tag. Observe that there are two tags of same name, but the latter one has a slash / before it, it is a closing tag. Now, what is a closing tag? Let's start with different types of tags!

Syntax
```
<p> Content </p>
```

### Types Of HTML Tags
There are two types of HTML Tags which are used by the website developers:
 1. Paired Tags (Open and Close Tags)
 2. Unpaired Tags (Singular Tags)

#### Paired Tags
Paired tags are a set of two tags with the same name. In each Paired tag set, one is an opening tag, and the other one is the closing tag. The closing tag has a / slash, it means that the tag is closed now.

It is necessary to close a paired tag; otherwise, it can result in the malfunctioning of the website. When the content is written within paired tags, then it ensures that the effect of those tags would be limited to only the content between them.

Look at the list of some paired tags in HTML below. Notice that each tag has a closing tag with a slash(/) before the name of the tag.

```Syntax: <tag> Content </tag>```
```
List of some paired tags in HTML:
    Open Tag	          Close Tag
    <html>	            </html>
    <table>	            </table>
    <form>	            </form>
    <span>	            </span>
    <ul>	              </ul>
    <p>	                </p>
    <head>	            </head>
    <div>	              </div>
```
#### Unpaired Tags (Singular Tags)
Unpaired tags are single tags with no closing tag. These tags are also called Singular Tags. These are also called non-container tags because they do not contain any content.

It is recommended to close the unpaired/singular tags also. But unfortunately, we do not have the closing tag for those. So, an unpaired tag is closed after adding a slash(/) just before the greater than > sign. ```For example: <br />```.

Look below the list of some Unpaired Tags in HTML. Notice the use of slash(/) in the tags, to close them.

```
Some Unpaired Tags are:
Open Tag
<br />
<hr />
<meta />
<input />
```
### HTML Heading Tag
Heading tag is used to give headings of different sizes in a document. There are six different HTML heading tags, which gives different heading sizes and are defined by ```<h1>``` to ```<h6>``` tags. ```<h1>``` gives the largest heading and ```<h6>``` gives the smallest one. So ```<h1>``` can be used for most important headings and ```<h6>``` can be used for a least important one.

```
EXAMPLE
<!DOCTYPE html> 

<html lang="en">

<head>

 <meta charset="UTF-8">

 <title> HTML Heading Tag </title>
 
</head> 


<body> 


<h1> This is Heading 1 </h1>
 
<h2> This is Heading 2 </h2> 

<h3> This is Heading 3 </h3> 

<h4> This is Heading 4 </h4> 

<h5> This is Heading 5 </h5> 

<h6> This is Heading 6 </h6> 


</body> 

</html> 
```
Gives the output:
<h1> This is Heading 1 </h1>
 
<h2> This is Heading 2 </h2> 

<h3> This is Heading 3 </h3> 

<h4> This is Heading 4 </h4> 

<h5> This is Heading 5 </h5> 

<h6> This is Heading 6 </h6> 

### HTML Paragraph Tag
The ```<p>``` tag is used to define a paragraph in a document. HTML paragraph or HTML ```<p>``` tag gives the text inside it, a paragraph like finishing. It is a notable point that a browser itself add an empty line before and after a paragraph.

Let's take a simple example to see how it works.
```
EXAMPLE



<!DOCTYPE html>
 
<html lang="en">

<head>

 <meta charset="UTF-8">

 <title> HTML Paragraph Tag </title>
 
</head> 


<body> 


<p> This is First Paragraph </p>
 
<p> This is Second Paragraph </p> 

<p> This is Third Paragraph </p> 


</body> 

</html> 
```

Gives the output:
<p> This is First Paragraph </p>
<p> This is Second Paragraph </p> 
<p> This is Third Paragraph </p> 

### HTML Anchor Tag
HTML Hyperlink is defined with the ```<a>``` tag (Anchor tag). It is used to give a link to any file, webpage, image etc.

This tag is called anchor tag and anything between the opening ```<a>``` tag and the closing ```</a>``` tag becomes part of the link, and a user can click that part to reach to the linked document.

 
Following is the simple syntax to use ```<a>``` tag.
```
EXAMPLE
<!DOCTYPE html> 

<HTML lang="en">  

<head> 

 <meta charset="UTF-8">

 <title> HTML Anchor Tag </title> 
	
</head> 

<body>  


<a target="_blank" href="https://www.coderepublics.com"> This is a link </a> 
 

</body>  

</html> 
```

Gives the output:
<a target="_blank" href="https://www.coderepublics.com"> This is a link </a>

### HTML Image Tag
The Image Tag is used to add Images in HTML documents. The HTML ```<img>``` tag is used to add image in a document. The 'src' attribute is used to give source(address) of the image. The height and width of the image can be controlled by the attributes - ```height="px"``` and ```width="px"```.

The ```'alt'``` attribute is used as an alternative in a case if the image is not shown. Anything written as a value of this attribute will be displayed. It will give information about the image.

```
EXAMPLE

<!DOCTYPE html> 

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> HTML Image Tag </title>
 
</head> 


<body> 


<img src="HTML-Image.png" width="400px" height="200px">


</body> 

</html> 
```

Gives the output:

<img src="https://www.coderepublics.com/tryit/HTML-Image.png" width="400px" height="200px">


### HTML Break Tag ```<br>```
The HTML <br> tag creates a line break within a paragraph. This tag is used very commonly during writing content for the website. The break tags are very helpful to write any content with line breaks. For example, writing a Poem or an address. In these type of content, the line break is very significant, so Break Tag helps to produce those line breaks without changing the paragraph.

The <br> tag is an Unpaired tag which means that it has no closing tag. Look at the example below to see how to use it:
```
EXAMPLE
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> HTML Break Line (br) Tag </title>

</head>

<body>


<p> To break lines <br> in a text, <br> use the br element. </p>


</body>

</html>
```
Gives The Output:
<p> To break lines <br> in a text, <br> use the br element. </p>


```
EXAMPLE

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> HTML Break Line (br) Tag </title>

</head>

<body>


<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 

labore et dolore magna aliqua. <br>Ut enim ad minim veniam, quis nostrud exercitation ullamco 

laboris nisi ut aliquip ex ea commodo consequat. <br><br> Duis aute irure dolor in 

reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 

sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 

</p>


</body>

</html>
```
Gives the output:
<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. <br>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. <br><br> Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. </p>

#### Difference between ```<br>``` and ```<br/>```
HTML ```<br>``` tag can be used in two ways: The ```<br>``` or ```<br/>```. It is recommended to use closed br tag ```<br/>```, because it is supported in both HTML and XHTML.


## HTML Attributes
HTML attribute defines the characterstics of any HTML element. These attributes provide additional information to the browser about the element like, its size, color, behaviour, etc.

### Some important points regarding HTML Attributes
	1.Attributes provide additional information about an element.
	2.Attributes are always specified in the start tag.
	3.Attributes usually come in name/value pairs like: name="value".
	4.Ex.- 'src' in <img> tag OR 'href' in <a> tag,etc..

### HTML Lang Attribute
The 'lang' attribute is declared in the opening <HTML> tag. It gives information to the browser about the main language used in the html document. Although it is not necessary to use but using it is a good practice.

You can check all the values of lang attribute for different languages from [here](https://www.coderepublics.com/Reference/html-language-code-names.php).

```
EXAMPLE

<!DOCTYPE html> 

<HTML lang="en">  

<head> 

  <meta charset="UTF-8">

  <title> HTML Lang Attribute </title>
 
</head> 


<body> 


<p> This page is using English Language. </p>


</body> 

</html> 
```

### HTML Title Attribute
The ```Title``` attribute is used to specify a tooltip. That tooltip could be some important piece of information in text form. It is often displayed when cursor comes over the element or while the element is loading.

Adding tooltips using Title attribute, is a smart way to give brief explanations about some element on the webpage. Look at the example below, to see how you can use it with any HTML tag.

```
EXAMPLE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> HTML Title Attribute </title>
</head>
<body>

<p><abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>
<p title="Free Web tutorials">CodeRepublics.com</p>

</body>
</html>
```

Gives the Output:
<p><abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>
<p title="Free Web tutorials">CodeRepublics.com</p>

Hover cursor over the Words "WHO" and "CodeRupclics.com" to see their embedded Titles.

### HTML Src Attribute
The ```src``` or (source) attribute is used with ```<img>``` tag. This attribute allows us to provide the path for the image to be included on the webpage. it is also used with ```<audio>``` tag, ```<video>``` tag, ```<embed>``` tag, etc. to add the source path of the file to be included.


### HTML alt Attribute
The ```alt``` attribute specifies an alternative text for an image. If somehow the browser is not able to display an image, then the alternate text will be displayed, which will give the information about the image. Also, value of alt attribute can be read by screen readers, which helps visually impaired person to "hear" information about the image.

If a browser cannot find an image, it will display the value of the alt attribute :
```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> HTML Image src Attribute </title> 
<body>

<img src="HTML5-Image.png" alt="HTML5 Image" style="width:600px; height:250px;">

</body>
</html>
```

Gives the output:

<img src="https://www.coderepublics.com/tryit/HTML5-Image.png" alt="HTML5 Image" style="width:600px; height:250px;">

### HTML style Attribute
The ```style``` attribute is used to specify the inline style of an element, i.e., it defines the CSS styling of element like color, font, size, shadow etc.
```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> Inline Style </title>	
</head>
<body>

<h4 style="color:green"> This is Green Color </h4>  
<h4 style="color:blue"> This is Blue Color </h4>  	

</body>
</html>  
```

## HTML Formatting Tags
HTML Formatting Tags are used to change appearance of text for better look and feel than the default text. The formatting tags can make text <b>bold, italic, underlined</b>, etc.

All the formatting tags are paired tags. Anything written between any formatting tag will be displayed according to the tag in the browser. For example, anything written between ```<i>``` and ```</i>``` will display as italic text in the browser.

There are different tags for various formatting tags. Each Tag has its own type of formatting associated with it.

### Some HTML Formatting tags are
	-Bold Tag <b>
	-Italic Tag <i>
	-Underline Tag <u>
	-Strong Tag <strong>
	-Small Tag <small>
	-Big Tag <big>
	-Mark Tag <mark>
	-Emphasized Tag <em>
	-Deleted Tag <del>
	-Inserted Tag <ins>
	-Subscripted Tag <sub>
	-Superscripted Tag <sup>

### HTML Bold Tag
The HTML ```<b>``` Tag defines bold text. Bold text is wider and darker text than the default text, without any extra importance to the browser. Look at the example below.

```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> Bold Text </title> 
</head> 

<body> 

<p> This is Normal text. </p> 
<b> This is Bold Text. </b> 

</body> 
</html>   
```
The output is:
<p> This is Normal text. </p> 
<b> This is Bold Text. </b> 

### HTML Strong Text
The HTML ```<strong>``` Tag displays same formatting like a ```<b>``` tag. But the Strong text has some importance to the browser and search engines. It is always recommended to write keywords within ```<strong>``` Tag to give them extra importance.

```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
<title> Strong Text </title> 
</head> 
<body> 

<p> This is Normal text </p> 
<strong> This Text is Strong </strong> 

</body> 
</html>   
```

The output will be:
<p> This is Normal text </p> 
<strong> This Text is Strong </strong> 

### HTML Italic Text
The HTML ```<i>``` Tag defines <i>italic</i> text. This type of formatting displays cursive font based text that slant slightly to the right.

```
EXAMPLE
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Italic Text </title>
 
</head> 

<body> 


<p> This is normal text </p>
 
<i> This is italic Text </i> 


</body> 

</html> 
```
The output is:
<p> This is normal text </p>
<i> This is italic Text </i> 

### HTML Underlined Text
The HTML ```<u>``` Tag defines Underlined text. All the text within the ```<u>``` and ```</u>``` tags will have an underline throughout.

Underlined Text is used to draw attention of the user and is a default formatting for a hyperlinked text.

```
EXAMPLE

<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Underlined Text </title>
 
</head> 


<body> 


<p> This is Normal text </p>
 
<u> This is Underlined Text </u> 


</body> 

</html> 
```

### HTML Small Text
The HTML ```<small>``` Tag defines small text. This text is used for some side commenting or to write some copyright information.

```
EXAMPLE


<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Small Text </title>
 
</head> 


<body> 


This text is <small> small </small>.


</body> 

</html>
```
### HTML Big Text
The HTML ```<mark>``` Tag defines Highlighted text. The text will have a background color and represent relevancy in an HTML document.

```
EXAMPLE
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Mark Tag </title>
 
</head> 


<body> 


This text is <mark> Marked. </mark>
 

</body> 

</html> 
```

### HTML Emphasized Text
The HTML ```<em>``` element defines Emphasized text. It will give the text the same Italic formatting. This tag is important for screen readers. The screen readers give extra emphasize on this type of text and read it with verbal stress.

```
EXAMPLES

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> Emphasize Tag </title> 
</head> 

<body> 

This text is Normal.  
This text is <em> Emphasized. </em> 

</body> 
</html>   
```
The ouput is:
This text is Normal.  
This text is <em> Emphasized. </em> 

### HTML Deleted Text
The HTML ```<del>``` element defines Deleted text. This displays Text with a line strike.
	
```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> Delete Text </title> 
</head> 

<body> 

<del> This text is deleted </del>

</body> 
</html>   
```
The output is 

<del> This text is deleted </del>


### HTML Inserted Text
The HTML ```<ins>``` element defines inserted (added) text. It gives the underlined formatting to the text. It is used in combination with deleted text.

```
EXAMPLE
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Insert Text </title> 

</head> 


<body> 


This text is <ins> inserted. </ins> 


</body> 

</html> 
```

The output is

This text is <ins> inserted <ins>

### HTML Subscripted Text
The HTML ```<sub>``` element defines <sub>subscripted</sub> text. This type of text is small in size and is placed slightly below the normal line of text.
	
```
EXAMPLE
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Subscript Text </title>
 
</head> 


<body> 


This text is <b> bold. </b>
 
This text is <i> italic. </i> 

This text is <sub> Subscripted. </sub> 


</body> 

</html> 
```
The output is

This text is <b> bold. </b>
This text is <i> italic. </i> 
This text is <sub> Subscripted. </sub>


### HTML Superscripted Text
The HTML ```<sup>``` element defines <sup>superscripted</sup> text. It also dispalys very small text like subscript, but here, the text is placed slightly above the normal line of text.

```
EXAMPLE
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="UTF-8">

  <title> Superscript Tag </title> 

</head> 


<body> 


This text is <b> bold. </b>
 
This text is <i> italic. </i>

This text is <sup> Superscripted. 


</body> 

</html> 
```

The output is

This text is <b> bold. </b>
This text is <i> italic. </i>
This text is <sup> Superscripted. 

## HTML Tables
We all are familiar with the concept of table, we are not talking about the numeric tables here, the HTML table we are going to learn is the one with rows and column. It’s similar like the structure of a matrix with proper rows and columns. This type of structure with rows and columns is very helpful in representing data in an easy and simple manner. The tabular form of data creates a good expression wherever it is used due to its representation of necessary data in a simple and accurate manner.

### Use of HTML Table ?
An HTML table is defined with the ```<table>``` tag. A table is used to display data in tabular form (rows * column). It is a paired tag. Just use these tags with their attributes to create tables. You can also use CSS stylesheet to beautify these structures. A table structure is represented in ‘rows*columns’ form, i.e. a ‘4*5’ table represents a table with 4 rows and 5 columns.

Tables are also used in websites to present any data to the user. It looks really neat and also everyone prefers tabular form of data nowadays. The HTML tables allows to arrange data like text, images, etc. into rows and columns.

```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> HTML Table Tag Examples </title> 
</head>

<body> 
<table> 
<tr> 
    <th> Name </th> 
    <th> Salary </th> 
    <th> Age </th> 
</tr>
<tr> 
    <td> Anshuman </td> 
    <td> Rs. 2,00,000 </td> 
    <td> 25 </td> 
</tr> 
<tr> 
    <td> Kuldeep </td> 
    <td> Rs. 5,00,000 </td> 
    <td> 22 </td> 
</tr> 
</table> 

</body> 
</html>
```

The output is

<table> 
<tr> 
    <th> Name </th> 
    <th> Salary </th> 
    <th> Age </th> 
</tr>
<tr> 
    <td> Anshuman </td> 
    <td> Rs. 2,00,000 </td> 
    <td> 25 </td> 
</tr> 
<tr> 
    <td> Kuldeep </td> 
    <td> Rs. 5,00,000 </td> 
    <td> 22 </td> 
</tr> 
</table> 

### Table Row
A table row can be defined with the ```<tr>``` tag It is also a paired tag with ```</tr>``` as a closing tag. Whatever written between these tags will be displayed in a single row of the table. To create a new row another ```<tr>``` tag is written after closing the previous one.

### Table heading
A table header in HTML tables is a special case of a table row. It starts with ```<th>``` tag and ends with ```</th>``` tag. There only difference between a row and a heading is that text written inside ```<th>``` tags is displayed in bold fonts and is by default centered aligned by the browser. Because of its properties this tag is used only for writing Heading of the table. You can also make a ```<tr>``` tags content bold and centered by using CSS It will work exactly like ```<th>``` tag.

### Table Cells
A table cell in an HTML table is defined by ```<td>``` tag. It is also a paired tag with ```</td>``` as a closing tag. Each pair of these tags represents a cell in a row. It is used inside ```<tr>``` tags only. Without ```<tr>``` tags it is of no value. After declaring the rows the ```<td>``` tags are used to enter data in the table. Whatever is written inside the ```<td>``` and ```</td>``` tags will be displayed by the browser in the tables as it is.

### Table Attributes
The ```<table>``` Tag in HTML table has many attributes which can be used to further define the structure of the table than just a standard one. These attributes can make a table look a bit more attractive. Let’s see one by one the different attributes of the table tag and then we will use them in an example and will see the changes in the table.

### The 'border' Attribute
A border attribute is used to specify visible borders in a table. It means that by default the borders in the table are hidden and if you don’t specify borders then your table will only display data but there would be no border between them. The border attribute has two values 0 and 1. 0 means no border and 1 means visible borders. You can also increase the values to 2, 3, 4, etc. it will increase the width of the border.

###### There are two ways to specify border for HTML tables.

	1. By "border" attribute of table in HTML
	2. By "border property" in CSS

```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> HTML Table Border Attribute </title> 
</head>

<body> 
<table border="1" width="100%"> 
<tr> 
    <th> Name </th> 
    <th> Salary </th> 
    <th> Age </th> 
</tr> 
<tr> 
    <td> Anshuman </td> 
    <td> Rs. 2,00,000 </td> 
    <td> 25 </td> 
</tr> 
<tr> 
    <td> Kuldeep </td> 
    <td> Rs. 5,00,000 </td> 
    <td> 22 </td> 
</tr> 
</table>

</body>
</html>  
```
The output obtained is

<table border="1" width="100%"> 
<tr> 
    <th> Name </th> 
    <th> Salary </th> 
    <th> Age </th> 
</tr> 
<tr> 
    <td> Anshuman </td> 
    <td> Rs. 2,00,000 </td> 
    <td> 25 </td> 
</tr> 
<tr> 
    <td> Kuldeep </td> 
    <td> Rs. 5,00,000 </td> 
    <td> 22 </td> 
</tr> 
</table>

The ```width``` attribute is used to sizing the table.

### Table CSS Border
You can use CSS Style to make table more interactive.

```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> HTML Table Border Style </title> 

  <style>
    table, th, td {
    border: 1px solid black;
    text-align: center;
        }
</style>

</head>

<body> 
<table width="100%"> 
<tr> 
    <th> Name </th> 
    <th> Salary </th> 
    <th> Age </th> 
</tr> 
<tr> 
    <td> Anshuman </td> 
    <td> Rs. 2,00,000 </dh> 
    <td> 25 </td> 
</tr> 
<tr> 
    <td> Kuldeep </td> 
    <td> Rs. 5,00,000 </td> 
    <td> 22 </td> 
</tr> 
</table>

</body>
</html>  
```

### The 'Cellpadding' and 'Cellspacing' Attribute
These "cellpadding" and "Cellspacing" attributes are used to adjust the white spaces in your table cells.

#### Cellpadding attribute
The Cellpadding attribute is used to specify the space between the content of the cell and its borders. It provides padding to the content of the cell. As its value increases the space between the cell’s content and its border is also increases. The value of this attribute is taken in pixels by the browser. The cellpadding is applied to all the four sides of the content. The value can also be defined in percentages.

#### Cellspacing attribute
The Cellspacing attribute is used to specify the space between the cells of the table. Its value can be in pixels or in percentages. It works similar to the Cellpadding attribute but only between cells. It is applied to all the sides of the cells.

Note: These two attributes defined above are no longer a part of HTML 5. So it is better to use CSS to color the tables.

```
EXAMPLE

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> HTML Table Cellpadding Attribute </title> 
</head>

<body>

<table border="1" cellpadding="5" cellspacing="5" style="width:100%">
<tr>
<th>Name</th>
<th>Salary</th>
</tr>
<tr>
<td>Peter</td>
<td>5000</td>
</tr>
<tr>
<td>John</td>
<td>7000</td>
</tr>
</table>

</body>
</html>  
```

### The 'Colspan' and 'Rowspan' Attribute

These two attributes are used with the ```<td>``` tag. As the name suggests colspan is related to columns and rowspan is related to rows. These two attributes are used to merge two or more columns and rows. The colspan attributes value suggest the amount of column space it will occupy. For example ```<td colspan= 2>``` will create a cell taking space of two cells horizontally i.e. it will occupy the space of a cell of the next column. Similarly, the rowspan will create a cell which will occupy the space of two or more (as specified) cells vertically, i.e. cells of the next rows. Look at the example below to understand the concept clearly.

#### The 'Rowspan'
The rowspan attribute is used to merge two or more rows together to form a single row. A single row occupies space of the number of merged rows.

```
EXAMPLE

<!DOCTYPE html>
<html>
    <html lang="en">
<head>
    <meta charset="UTF-8">
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    text-align: left;    
}
</style>
</head>
<body>

<h2>Cell that spans two rows:</h2>
<table style="width:100%">
  <tr>
    <th>Name:</th>
    <td>Bill Gates</td>
  </tr>
  <tr>
    <th rowspan="2">Telephone:</th>
    <td>9998887776</td>
  </tr>
  <tr>
    <td>9998887776</td>
  </tr>
</table>

</body>
</html>
```

#### The 'Colspan'
The colspan attribute is used to merge two or more columns into a single column. single column occupies space of the number of merged columns.

```
EXAMPLE

<!DOCTYPE html>
<html>
<html lang="en">
<head>
    <meta charset="UTF-8">
  <title> HTML Table Colspan Attribute </title>
</head>
<body>
  
<table border="1" width="80%"> 
<tr> 
    <th> Person_Name </th> 
    <th colspan="2"> Mobile </th> 
    </tr> 

<tr> 
    <td> Bill Gates </td> 
    <td> 9998887776 </td> 
    <td> 9998887775 </td> 
</tr> 
</table>

</body>
</html>
```
The output will be

<table border="1" width="80%"> 
<tr> 
    <th> Person_Name </th> 
    <th colspan="2"> Mobile </th> 
    </tr> 

<tr> 
    <td> Bill Gates </td> 
    <td> 9998887776 </td> 
    <td> 9998887775 </td> 
</tr> 
</table>

### HTML Caption
To add a caption to a table, use the <caption> tag.
A caption can be aligned around the table by using align attribute with values -left/right/top/bottom.
The default alignment is top.

```
EXAMPLE

<!DOCTYPE html>
<html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> HTML Table Caption Attribute </title>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
<body>

<table>
  <caption>Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$50</td>
  </tr>
</table>

</body>
</html>
```

The output is

<table>
  <caption>Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$50</td>
  </tr>
</table>

### Height and Width attributes
The Height and Width attributes of an HTML table are used to specify the height and width of the table. Their value can be specified in terms of pixels or percentages.

### bgcolor attribute attribute
This attribute in HTML table is used to provide a background color to the table. You can easily write any color name directly or you can also set a color by providing HEX code. This attribute can also be used with ```<td>``` tag to define the color of that particular cell in the table.

### background attribute
This attribute in HTML table is used to add a background image in the table. The image in the table will work as a background behind the data in the table. It is also can be used with ```<td>``` tag.
