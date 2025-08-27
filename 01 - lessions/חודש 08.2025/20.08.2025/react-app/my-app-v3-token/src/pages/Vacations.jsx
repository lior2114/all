import React, { useState } from 'react';
import { getVacations } from '../api/apiVacations';

const Vacations = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFetchVacations = async () => {
        setLoading(true);
        setError(null);
        
        try {
            console.log('Fetching vacations...');
            const vacations = await getVacations();
            console.log('All vacations:', vacations);
            console.log('Number of vacations:', vacations.length);
            
            // Additional debug info
            if (vacations.length > 0) {
                console.log('First vacation details:', vacations[0]);
                console.log('Vacation IDs:', vacations.map(v => v.id || v.vacation_id));
            }
            
        } catch (error) {
            console.error('Error fetching vacations:', error);
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Vacations</h1>
            <p>Explore our amazing vacation destinations!</p>
            
            <div style={{ marginTop: '20px' }}>
                <button 
                    onClick={handleFetchVacations}
                    disabled={loading}
                    style={{
                        padding: '10px 20px',
                        fontSize: '16px',
                        backgroundColor: '#007bff',
                        color: 'white',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: loading ? 'not-allowed' : 'pointer',
                        opacity: loading ? 0.6 : 1
                    }}
                >
                    {loading ? 'Loading...' : 'Fetch All Vacations (Debug)'}
                </button>
                
                {error && (
                    <div style={{ 
                        marginTop: '10px', 
                        color: 'red', 
                        padding: '10px',
                        backgroundColor: '#ffe6e6',
                        borderRadius: '5px'
                    }}>
                        Error: {error}
                    </div>
                )}
                
                <div style={{ marginTop: '20px', fontSize: '14px', color: '#666' }}>
                    <p>💡 <strong>Debug Info:</strong></p>
                    <p>• Click the button above to fetch all vacations</p>
                    <p>• Check the browser console for the results</p>
                    <p>• Make sure you're logged in (token required)</p>
                </div>
            </div>
        </div>
    );
};

export default Vacations;