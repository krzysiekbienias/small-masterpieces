# Small Masterpieces

Small Masterpieces is a collection of compact yet powerful projects, each designed to solve a specific problem with clean and efficient code. This repository serves as a playground for exploring algorithms, utility functions, and small-scale applications.

# Calculator

# Dragon polymorphism in practice
Dragon Unit Simulation

📌 Overview

This project simulates a unit-based system where different entities, including Dragons, interact in a 2D coordinate space. Unlike standard units, Dragons occupy an area instead of a single point, allowing for collision detection, interactions, and movement constraints.

🏗️ Structure

### 1️⃣ Unit Class

The Unit class represents a basic entity in a 2D world, identified by its position (pos_x, pos_y). It is treated as a point on the map.

Unit Attributes:

`name` → Unit's name.

`pos_x`, `pos_y` → Coordinates representing its position.

Unit Methods:

`in_area(x1, y1, x2, y2)` → Checks if the unit (as a point) is inside a rectangular region.

### 2️⃣ Dragon Class 🐉

The Dragon class extends Unit, but instead of being a point, it occupies a rectangular space on the map.

Dragon Attributes:

* Inherits name, pos_x, pos_y from Unit.

* `fire_range` → The distance a dragon can attack with fire.

* `height` & `width` → Define the dragon's physical size.

* `__hit_box` → A `Rectangle` that represents the dragon's occupied area.

Dragon Methods:

* `in_area(x1, y1, x2, y2)` → Checks if the dragon's hitbox overlaps with a given area (e.g., another dragon, an attack zone, a restricted region).

### 3️⃣ Rectangle Class 🟥

Used to represent occupied areas (such as a Dragon's hitbox) and to check for overlaps (collisions).

Rectangle Methods:

`overlaps(rect)` → Determines if two rectangles overlap.

`get_left_x()`, `get_right_x()`, `get_top_y()`, `get_bottom_y()` → Retrieve boundary values.

### 🚀 How It Works

A Dragon is defined by its center position (pos_x, pos_y), but it spans a rectangular region.

When `in_area(x1, y1, x2, y2)` is called:

A Rectangle object is created representing the given area.

The method checks whether this rectangle overlaps with the Dragon’s __hit_box.

This enables:

* Collision detection between dragons 🐉 vs 🐉.

* Interaction checks (e.g., is the dragon inside an attack zone?).

* Pathing restrictions (e.g., preventing dragons from overlapping certain areas).
