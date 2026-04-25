//Configuracion de URLs
const API_BASE_URL = 'http://localhost:500/api';

document.addEventListener('DOMContentLoaded', () => {
    checkBackendStatus();
    fetchTeamData();
});

// Función para el indicador de estado 
async function checkBackendStatus() {
    const statusIndicator = document.getElementById('status-indicator');
    try{
        const response = await fetch (`${API_BASE_URL}/health`);
        if (response.ok){
            statusIndicator.textContent= 'Online';
            statusIndicator.style.color= 'green';
        }else {
            throw new Error();
        }

    } catch (error){
        statusIndicator.textContent= 'Offline';
        statusIndicator.style.color= 'red';
    }
}

// Funcion para obtener los integrantes

async function fetchTeamData() {
    const tableBody = document.getElementById('team-table-body');
    try {
        const response = await fetch(`${API_BASE_URL}/team`);
        const data = await response.json();
        
        //lipiamos tabla antes de insertar
        tableBody.innerHTML= '';

        //Construcción dinámica de la tabla
        data.forEach(memeber=>{
            const row = document.createElement('tr');
            row.innerHTML=`
            <td>${memeber.nombre}</td>
            <td>${memeber.legajo}</td>
            <td>${memeber.feature}</td>
            <td>${memeber.servicio}</td>
            <td>${memeber.estado}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error){
        console.error('Error al cargar los datos del equipo:',error)
    }
}