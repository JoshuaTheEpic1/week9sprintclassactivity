#ifndef TASK_H
#define TASK_H

#include <string>

class Task {
public:
    std::string description;
    std::string title;
    std::string dueDate;
    bool is_completed;

    Task(const std::string& description, const std::string& title, const std::string& dueDate)
        : description(description), title(title), dueDate(dueDate), is_completed(false) {}

    std::string to_string() const;
};

#endif // TASK_H
