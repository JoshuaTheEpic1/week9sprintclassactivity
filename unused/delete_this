#ifndef TASKMANAGER_H
#define TASKMANAGER_H

#include <vector>
#include <string>

class TaskManager {
private:
    std::vector<Task> tasks;

public:
    TaskManager();

    void add_task(const std::string& title, const std::string& description, const std::string& due_date);
    Task* find_task_by_title(const std::string& title);
    void edit_task(const std::string& title, const std::string& new_title, const std::string& description, const std::string& due_date);
    void delete_task(const std::string& title);
    void mark_task_as_completed(const std::string& title);
    void sort_tasks(const std::string& by = "title", bool reverse = false);
    void filter_tasks(const std::string& title_contains = "", const std::string& due_date = "", bool completed = false);
    void print_tasks() const;
};

#endif // TASKMANAGER_H
