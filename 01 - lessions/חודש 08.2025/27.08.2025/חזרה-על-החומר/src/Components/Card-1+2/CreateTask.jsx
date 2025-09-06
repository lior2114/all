import { useTasks } from "../../Contexts/TasksContext"
import { TaskCard } from "./TaskCard"
import { Snackbar, Alert, CircularProgress, Box } from '@mui/material';

export const CreateTask = () => {

    const { title, setTitle, description, setDescription, newTasks, toggleTaskStatus, handleDelete, btlhandle, snackbarOpen, handleCloseSnackbar, isInitialLoading} = useTasks()

    // הצגת loading spinner בזמן הטעינה הראשונית
    if (isInitialLoading) {
        return (
            <Box 
                display="flex" 
                justifyContent="center" 
                alignItems="center" 
                minHeight="100vh"
                flexDirection="column"
                gap={2}
            >
                <CircularProgress size={60} />
                <div style={{ fontSize: '18px', color: '#666' }}>טוען...</div>
            </Box>
        );
    }

    return (
            <div>
                <input type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                />

                <input type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Description"
                />

                <button onClick={btlhandle}>
                    Add task
                </button>

                {newTasks.length === 0 ? (
                    <div>No cards yet</div>
                ) : (
                    newTasks.map((task) => (
                        <TaskCard 
                            key={task.id} 
                            id={task.id}
                            title={task.title} 
                            description={task.description}
                            done={task.done}
                            onToggle={toggleTaskStatus}
                            onToggleDelete={handleDelete}
                        />
                    ))
                )}

                <Snackbar
                    open={snackbarOpen}
                    autoHideDuration={4000}
                    onClose={handleCloseSnackbar}
                    anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
                >
                    <Alert onClose={handleCloseSnackbar} severity="success" sx={{ width: '100%' }}>
                        ברוך הבא! 🎉
                    </Alert>
                </Snackbar>
            </div>
            )
}