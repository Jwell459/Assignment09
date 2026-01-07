
export async function init() {
    const response = await fetch('../data/employees.json').then(response => response.json())
    return response
}