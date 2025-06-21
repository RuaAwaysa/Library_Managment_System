# Library Management System
Simplified fully functional Object-Oriented Python Library Management System  that incorporates abstraction, interfaces, exception handling, and custom class design.
## Features

* Add, delete, and view library items (Books, DVDs, Magazines).
* Register and delete users.
* Borrow and return items with availability checks.
* Search items by title or type.
* Search users by name or user ID.
* Data persistence using JSON files (`users.json` and `items.json`).
* Exception handling for common errors (e.g., user/item not found, item not available) and Any excepected error using user-define errors(e.g. UserNotFound, ItemNotAvailable)



## Technologies Used

* Python 3.x
* JSON for data storage

## Getting Started

### Prerequisites

* Python 3.x installed on your machine

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

## Usage

Run the main program:

```bash
python main.py
```

You will be presented with a menu to:

1. View all available items
2. Search items by title or type
3. Register as a new user
4. Borrow an item
5. Return an item
6. Delete a user
7. Delete an item
8. View all users
9. Add a new item
10. Search for user by name or ID
11. Exit and Save

Follow the on-screen prompts to interact with the system.

## File Structure

```
library-management-system/
│
├── main.py                 
├── models/
│   ├── library.py          
│   ├── user.py             
│   ├── book.py             
│   ├── dvd.py              
│   └── magazine.py         
├── exceptions/
│   ├── item_not_found.py
│   ├── item_not_avilable.py
│   └── user_not_found.py
├── users.json              
└── items.json              
```

## Error Handling

* Handles file loading errors and empty files.
* Prevents borrowing unavailable items.
* Informs when users or items do not exist.
* Handles user input errors and unexpected interruptions (e.g., Ctrl+C).
