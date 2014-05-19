			КОНЗОЛНА СИСТЕМА ЗА БЕЛЕЖКИ
=============================================================================================



Системата ще дава възможност да се създават обекти от тип БЕЛЕЖКА, TODO, ПРЕДМЕТ
(в ядрото са първите два, ПРЕДМЕТЪТ е разширение):

    -Бележката ще представлява текст, като всяка бележка се създава, след което може да се
        редактира и изтрива.

    -TODO-то ще представлява текст, като има дати на започване и завършване, както и флаг,
	отбелязващ дали е завършено. Съответно този тип обекти имат възможност да създаване,
	редактиране, отбелязване като завършени, изтриване. Датата на зъвршване може да се 
	посочва от потребителя, но при отбелязване като завършено, тя се поставя автоматично.

    -Предметът отново предсталвява текст, като всеки предмет има местонахождение и притежател,
	може да се създава, редактира и изтрива.

Системата ще поддържа също възможност за търсене сред обектите. Може да се търси по тип обект или 
по неговите атрибути. Включва се и помощ за синтаксиса при търсене за типовете обекти, техните атрибути
и позволените стойности на атрибутите.

Всеки обект може да има произволен брой етикети. Едно от разширенията на системата е всеки етикет с име
"седмица" или "week" да се показва като съответно <<<седмица>>> и <<<week>>>.


Цел за Milestone2: Ядрото на системата (БЕЛЕЖКА и TODO) с основните им функционалности.
 



########################################################################################################################################




			CONSOLE NOTES SYSTEM
=============================================================================================



The system gives the opportunity objects of the following types to be created: 	NOTE, TODO, SUBJECT
(the first two of them are in the core, the SUBJECT is an extention):
    
    -The note is a text. Each note is created and could be edited and erased after that.

    -The TODO  is also a text and it has date of beginning and date of finnishig and also a flag,
marking if it has been finnished. The date of finnishing could be set by the user, but it is automatically 
set if the TODO has been marked as finnished.

    -The subject is also a text. It has location and owner, it can be created, edited, erased.

The system also supports the opportunity for searching among the objects. The user can search by type of object 
or by object's attributes. Help for the syntax while searching is also included.

Each object has labels. One of the system's extentions is each label with name "седмица" or "week" to be shown as 
<<<седмица>>> or <<<week>>>.


Goal for Milestone 2: The core of the system (NOTE and TODO) with their main functionallities.

