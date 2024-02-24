import api from "api/utils/api";
import { Donation, FetchDonationsParams } from "../models";

export namespace BloodDonationsEndpoint {
  export const fetchBloodDonations = async (params: FetchDonationsParams) => {
    return api.get<Donation[]>("/api/blood-donations/", { params });
  };

  export const postBloodDonation = async (donationId: number, petId: number) => {
    return api.post<Donation>(`/api/blood-donations/${donationId}/pet/${petId}`, {
      msg: "string",
      amount: 0
    });
  };
}
