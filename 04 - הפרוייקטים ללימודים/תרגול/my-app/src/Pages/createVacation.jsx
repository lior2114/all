import { useState } from "react"
import { useVacation } from "../Contexts/vacationContext"


export function CreateVacation(){

    const {createVacation,error} = useVacation()
    const [form, setForm] = useState({
        country_id: "",
        vacation_name: "",
        vacation_description: "",
        vacation_start: "",
        vacation_ends: "",
        vacation_price: "",
        vacation_file_name: ""
    })

    const handleForm = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            await createVacation(form)
        } catch (error) {
            console.error("Error creating vacation:", error)
        }
    }

    return(
        <>
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="countryId">Country ID:</label>
                <input
                    type="number"
                    id="countryId"
                    name="country_id"
                    value={form.country_id}
                    onChange={handleForm}
                    required
                />
            </div>

            <div>
                <label htmlFor="vacationName">Vacation Name:</label>
                <input
                    type="text"
                    id="vacationName"
                    name="vacation_name"
                    value={form.vacation_name}
                    onChange={handleForm}
                    required
                />
            </div>

            <div>
                <label htmlFor="vacationDescription">Vacation Description:</label>
                <textarea
                    id="vacationDescription"
                    name="vacation_description"
                    value={form.vacation_description}
                    onChange={handleForm}
                    required
                />
            </div>

            <div>
                <label htmlFor="vacationStart">Start Date:</label>
                <input
                    type="date"
                    id="vacationStart"
                    name="vacation_start"
                    value={form.vacation_start}
                    onChange={handleForm}
                    required
                />
            </div>

            <div>
                <label htmlFor="vacationEnds">End Date:</label>
                <input
                    type="date"
                    id="vacationEnds"
                    name="vacation_ends"
                    value={form.vacation_ends}
                    onChange={handleForm}
                    required
                />
            </div>

            <div>
                <label htmlFor="vacationPrice">Price:</label>
                <input
                    type="number"
                    step="0.01"
                    id="vacationPrice"
                    name="vacation_price"
                    value={form.vacation_price}
                    onChange={handleForm}
                    required
                />
            </div>

            <div>
                <label htmlFor="vacationFileName">Image File Name:</label>
                <input
                    type="text"
                    id="vacationFileName"
                    name="vacation_file_name"
                    value={form.vacation_file_name}
                    onChange={handleForm}
                    required
                />
            </div>
            {error && <p style={{color: 'red'}}>{error}</p>}

            <button type="submit">Create Vacation</button>
        </form>
        </>
    )
}